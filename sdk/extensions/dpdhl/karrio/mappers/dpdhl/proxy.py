"""Karrio Deutsche Post DHL client proxy."""
import urllib.parse
import karrio.lib as lib
import karrio.api.proxy as proxy
import karrio.universal.mappers.rating_proxy as rating_proxy
import karrio.mappers.dpdhl.settings as provider_settings


class Proxy(rating_proxy.RatingMixinProxy, proxy.Proxy):
    settings: provider_settings.Settings

    def get_rates(self, request: lib.Serializable) -> lib.Deserializable:
        return super().get_rates(request)

    def create_shipment(self, request: lib.Serializable) -> lib.Deserializable[str]:
        response = lib.request(
            url=f"{self.settings.server_url}/soap",
            data=request.serialize(),
            trace=self.trace_as("xml"),
            method="POST",
            headers={
                "Authorization": f"Basic {self.settings.basic_authentication}",
                "SOAPAction": "urn:createShipmentOrder",
            },
        )

        return lib.Deserializable(response, lib.to_element)

    def cancel_shipment(self, request: lib.Serializable) -> lib.Deserializable[str]:
        response = lib.request(
            url=f"{self.settings.server_url}/soap",
            data=request.serialize(),
            trace=self.trace_as("xml"),
            method="POST",
            headers={
                "Authorization": f"Basic {self.settings.basic_authentication}",
                "SOAPAction": "urn:deleteShipmentOrder",
            },
        )

        return lib.Deserializable(response, lib.to_element)

    def get_tracking(self, requests: lib.Serializable) -> lib.Deserializable[str]:
        def _track(request):
            query = urllib.parse.urlencode(dict(xml=request))

            return lib.request(
                url=f"{self.settings.server_url}/rest/sendungsverfolgung?{query}",
                trace=self.trace_as("xml"),
                method="GET",
                headers={
                    "Authorization": f"Basic {self.settings.basic_authentication}",
                },
            )

        responses = lib.run_concurently(_track, requests.serialize())

        return lib.Deserializable(
            responses, lambda results: [lib.to_element(res) for res in results]
        )