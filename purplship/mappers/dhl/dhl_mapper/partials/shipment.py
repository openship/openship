import time
from base64 import b64decode
from pydhl.datatypes_global_v61 import MetaData
from pydhl import (
    ship_val_global_req_61 as ShipReq,
    ship_val_global_res_61 as ShipRes
)
from .interface import (
    reduce, Tuple, List, Union, T, DHLMapperBase
)


class DHLMapperPartial(DHLMapperBase):

    def parse_dhlshipment_respone(self, response) -> Tuple[T.ShipmentDetails, List[T.Error]]:
        return (self._extract_shipment(response), self.parse_error_response(response))

    def _extract_shipment(self, shipmentResponseNode) -> T.ShipmentDetails:
        """
            Shipment extraction is implemented using lxml queries instead of generated ShipmentResponse type
            because the type construction fail during validation out of our control
        """
        get_value = lambda query: query[0].text if len(query) > 0 else None
        get = lambda key: get_value(shipmentResponseNode.xpath("//%s" % key))
        tracking_number = get("AirwayBillNumber")
        if tracking_number == None:
            return None
        plates = [p.text for p in shipmentResponseNode.xpath("//LicensePlateBarCode")]
        barcodes = [child.text for child in shipmentResponseNode.xpath("//Barcodes")[0].getchildren()]
        documents = reduce(lambda r,i: (r + [i] if i else r), [get("AWBBarCode")] + plates + barcodes, [])
        reference = T.ReferenceDetails(value=get("ReferenceID"), type=get("ReferenceType")) if len(shipmentResponseNode.xpath("//Reference")) > 0 else None
        currency_ = get("CurrencyCode")
        return T.ShipmentDetails(
            carrier=self.client.carrier_name,
            tracking_numbers=[tracking_number],
            shipment_date= get("ShipmentDate"),
            services=(
                [get("ProductShortName")] +
                [service.text for service in shipmentResponseNode.xpath("//SpecialServiceDesc")] +
                [service.text for service in shipmentResponseNode.xpath("//InternalServiceCode")]
            ),
            charges=[
                T.ChargeDetails(name="PackageCharge", amount=float(get("PackageCharge")), currency=currency_) 
            ],
            documents=documents,
            reference=reference,
            total_charge= T.ChargeDetails(name="Shipment charge", amount=get("ShippingCharge"), currency=currency_)
        )

    def create_dhlshipment_request(self, payload: T.shipment_request) -> ShipReq.ShipmentRequest:
        is_dutiable = payload.shipment.declared_value != None
        default_packaging_type = "FLY" if payload.shipment.is_document else "BOX"
        extra_services = (
            [payload.shipment.service_type] +
            payload.shipment.extra_services +
            ([] if not payload.shipment.insured_amount else ["I"])
        )

        Request_ = self.init_request()
        Request_.MetaData = MetaData(SoftwareName="3PV", SoftwareVersion="1.0")

        return ShipReq.ShipmentRequest(
            schemaVersion="6.1",
            Request=Request_,
            RegionCode=payload.shipment.extra.get('RegionCode') or "AM",
            RequestedPickupTime=payload.shipment.extra.get('RequestedPickupTime') or "Y",
            LanguageCode=payload.shipment.extra.get('LanguageCode') or "en",
            PiecesEnabled=payload.shipment.extra.get('PiecesEnabled') or "Y",
            LatinResponseInd=None,
            Billing=ShipReq.Billing(
                ShipperAccountNumber=payload.shipper.account_number,
                BillingAccountNumber=payload.shipment.payment_account_number,
                ShippingPaymentType=payload.shipment.paid_by,
                DutyAccountNumber=payload.shipment.duty_payment_account,
                DutyPaymentType=payload.shipment.duty_paid_by
            ),
            Consignee=ShipReq.Consignee(
                CompanyName=payload.recipient.company_name,
                SuiteDepartmentName=None,
                AddressLine=payload.recipient.address_lines,
                City=payload.recipient.city,
                Division=payload.recipient.state,
                DivisionCode=payload.recipient.state_code,
                PostalCode=payload.recipient.postal_code,
                CountryCode=payload.recipient.country_code,
                CountryName=payload.recipient.country_name,
                FederalTaxId=payload.shipper.tax_id,
                StateTaxId=None,
                Contact=ShipReq.Contact(
                    PersonName=payload.recipient.person_name,
                    PhoneNumber=payload.recipient.phone_number,
                    Email=payload.recipient.email_address,
                    FaxNumber=payload.recipient.extra.get('FaxNumber'),
                    Telex=payload.recipient.extra.get('Telex'),
                    PhoneExtension=payload.recipient.extra.get('PhoneExtension'),
                    MobilePhoneNumber=payload.recipient.extra.get('MobilePhoneNumber')
                ) if any([payload.recipient.person_name, payload.recipient.phone_number, payload.recipient.email_address]) else None,
                Suburb=None
            ),
            Commodity=[
                ShipReq.Commodity(
                    CommodityCode=c.code, 
                    CommodityName=c.description
                ) for c in payload.shipment.items
            ],
            NewShipper=payload.shipment.extra.get('NewShipper'),
            Shipper=ShipReq.Shipper(
                ShipperID=payload.shipper.account_number,
                RegisteredAccount=payload.shipper.account_number,
                AddressLine=payload.shipper.address_lines,
                CompanyName=payload.shipper.company_name,
                PostalCode=payload.shipper.postal_code,
                CountryCode=payload.shipper.country_code,
                City=payload.shipper.city,
                CountryName=payload.shipper.country_name,
                Division=payload.shipper.state,
                DivisionCode=payload.shipper.state_code,
                Contact=ShipReq.Contact(
                    PersonName=payload.shipper.person_name,
                    PhoneNumber=payload.shipper.phone_number,
                    Email=payload.shipper.email_address,
                    FaxNumber=payload.shipper.extra.get('FaxNumber'),
                    Telex=payload.shipper.extra.get('Telex'),
                    PhoneExtension=payload.shipper.extra.get('PhoneExtension'),
                    MobilePhoneNumber=payload.shipper.extra.get('MobilePhoneNumber')
                ) if any([payload.shipper.person_name, payload.shipper.phone_number, payload.shipper.email_address]) else None
            ),
            ShipmentDetails=ShipReq.ShipmentDetails(
                NumberOfPieces=len(payload.shipment.items),
                Pieces=(lambda pieces:
                    (
                        pieces,
                        [
                            pieces.add_Piece(ShipReq.Piece(
                                PieceID=p.id,
                                PackageType=p.packaging_type or default_packaging_type,
                                Weight=p.weight,
                                DimWeight=p.extra.get('DimWeight'),
                                Height=p.height,
                                Width=p.width,
                                Depth=p.length,
                                PieceContents=p.content
                            )) for p in payload.shipment.items
                        ]
                    )[0]
                )(ShipReq.Pieces()),
                Weight=payload.shipment.total_weight or sum([p.weight for p in payload.shipment.items]),
                CurrencyCode=payload.shipment.currency or "USD",
                WeightUnit=(payload.shipment.weight_unit or "KG")[0],
                DimensionUnit=(payload.shipment.dimension_unit or "CM")[0],
                Date=payload.shipment.date or time.strftime('%Y-%m-%d'),
                PackageType=payload.shipment.packaging_type or payload.shipment.extra.get('PackageType'),
                IsDutiable= "N" if payload.shipment.is_document else "Y",
                InsuredAmount=payload.shipment.insured_amount,
                DoorTo=payload.shipment.extra.get('DoorTo'),
                GlobalProductCode=payload.shipment.extra.get('GlobalProductCode'),
                LocalProductCode=payload.shipment.extra.get('LocalProductCode'),
                Contents=payload.shipment.extra.get('Contents') or "..."
            ),
            EProcShip=payload.shipment.extra.get('EProcShip'),
            Dutiable=ShipReq.Dutiable(
                DeclaredCurrency=payload.shipment.currency or "USD",
                DeclaredValue=payload.shipment.declared_value,
                TermsOfTrade=payload.shipment.customs.terms_of_trade,
                ScheduleB=payload.shipment.customs.extra.get('ScheduleB'),
                ExportLicense=payload.shipment.customs.extra.get('ExportLicense'),
                ShipperEIN=payload.shipment.customs.extra.get('ShipperEIN'),
                ShipperIDType=payload.shipment.customs.extra.get('ShipperIDType'),
                ImportLicense=payload.shipment.customs.extra.get('ImportLicense'),
                ConsigneeEIN=payload.shipment.customs.extra.get('ConsigneeEIN')
            ) if is_dutiable else None,
            ExportDeclaration=None,
            Reference=[
                ShipReq.Reference(
                    ReferenceID=r
                ) for r in payload.shipment.references
            ],
            SpecialService=[
                ShipReq.SpecialService(
                    SpecialServiceType=service
                ) for service in extra_services
            ] if len(extra_services) > 0 else None,
            LabelImageFormat=payload.shipment.label.format if payload.shipment.label != None else None,
            DocImages=(lambda images:
                (
                    images,
                    [
                        images.add_DocImage(ShipReq.DocImage(
                            Type=doc.type,
                            ImageFormat=doc.format,
                            Image=b64decode(
                                doc.image + '=' * (-len(doc.image) % 4)
                            ) 
                        )) for doc in payload.shipment.doc_images
                    ]
                )[0]
            )(ShipReq.DocImages()) if len(payload.shipment.doc_images) > 0 else None,
            RequestArchiveDoc=None,
            NumberOfArchiveDoc=None,
            Label=None,
            ODDLinkReq=None,
            DGs=None
        )

