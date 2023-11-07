
import typing
import karrio.lib as lib
import karrio.core.units as units
import karrio.core.models as models
import karrio.providers.dhl_express.error as error
import karrio.providers.dhl_express.utils as provider_utils
import karrio.providers.dhl_express.units as provider_units


def parse_pickup_cancel_response(
    response: dict,
    settings: provider_utils.Settings,
) -> typing.Tuple[models.ConfirmationDetails, typing.List[models.Message]]:
    response_messages = []  # extract carrier response errors and messages
    messages = error.parse_error_response(response_messages, settings)
    success = True  # compute address validation success state

    confirmation = (
        models.ConfirmationDetails(
            carrier_id=settings.carrier_id,
            carrier_name=settings.carrier_name,
            operation="Cancel Pickup",
            success=success,
        ) if success else None
    )

    return confirmation, messages


def pickup_cancel_request(
    payload: models.PickupCancelRequest,
    settings: provider_utils.Settings,
) -> lib.Serializable:

    request = None  # map data to convert karrio model to dhl_express specific type

    return lib.Serializable(request)