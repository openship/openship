from typing import List, Tuple
from purplship.api.mapper import Mapper as BaseMapper
from purplship.mappers.ups_package.settings import Settings
from purplship.core.utils import Deserializable, Serializable, Envelope, Pipeline
from purplship.core.models import (
    RateRequest,
    ShipmentRequest,
    TrackingRequest,
    ShipmentDetails,
    RateDetails,
    TrackingDetails,
    Message,
    PickupRequest,
    PickupUpdateRequest,
    PickupCancellationRequest,
    PickupDetails,
    ConfirmationDetails,
)
from purplship.providers.ups import parse_track_response, track_request
from purplship.providers.ups.package import (
    parse_shipment_response,
    parse_rate_response,
    shipment_request,
    rate_request,
    create_pickup_pipeline,
    parse_pickup_response,
    update_pickup_pipeline,
    cancel_pickup_request,
    parse_cancel_pickup_response,
)
from pyups.rate_web_service_schema import RateRequest as UPSRateRequest
from pyups.track_web_service_schema import TrackRequest
from pyups.ship_web_service_schema import ShipmentRequest as UPSShipmentRequest


class Mapper(BaseMapper):
    settings: Settings

    """Request Mappers"""

    def create_rate_request(self, payload: RateRequest) -> Serializable[Envelope]:
        return rate_request(payload, self.settings)

    def create_tracking_request(
        self, payload: TrackingRequest
    ) -> Serializable[List[TrackRequest]]:
        return track_request(payload, self.settings)

    def create_shipment_request(
        self, payload: ShipmentRequest
    ) -> Serializable[UPSShipmentRequest]:
        return shipment_request(payload, self.settings)

    def create_pickup_request(self, payload: PickupRequest) -> Serializable[Pipeline]:
        return create_pickup_pipeline(payload, self.settings)

    def create_modify_pickup_request(
        self, payload: PickupUpdateRequest
    ) -> Serializable[Pipeline]:
        return update_pickup_pipeline(payload, self.settings)

    def create_cancel_pickup_request(
        self, payload: PickupCancellationRequest
    ) -> Serializable[Envelope]:
        return cancel_pickup_request(payload, self.settings)

    """Response Parsers"""

    def parse_rate_response(
        self, response: Deserializable[str]
    ) -> Tuple[List[RateDetails], List[Message]]:
        return parse_rate_response(response.deserialize(), self.settings)

    def parse_tracking_response(
        self, response: Deserializable[str]
    ) -> Tuple[List[TrackingDetails], List[Message]]:
        return parse_track_response(response.deserialize(), self.settings)

    def parse_shipment_response(
        self, response: Deserializable[str]
    ) -> Tuple[ShipmentDetails, List[Message]]:
        return parse_shipment_response(response.deserialize(), self.settings)

    def parse_pickup_response(
        self, response: Deserializable
    ) -> Tuple[PickupDetails, List[Message]]:
        return parse_pickup_response(response.deserialize(), self.settings)

    def parse_modify_pickup_response(
        self, response: Deserializable
    ) -> Tuple[PickupDetails, List[Message]]:
        return parse_pickup_response(response.deserialize(), self.settings)

    def parse_cancel_pickup_response(
        self, response: Deserializable
    ) -> Tuple[ConfirmationDetails, List[Message]]:
        return parse_cancel_pickup_response(response.deserialize(), self.settings)
