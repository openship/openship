/**
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2023.1rc
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
/**
 *
 * @export
 * @interface Webhook
 */
export interface Webhook {
    /**
     * A unique identifier
     * @type {string}
     * @memberof Webhook
     */
    id?: string;
    /**
     * The URL of the webhook endpoint.
     * @type {string}
     * @memberof Webhook
     */
    url: string;
    /**
     * An optional description of what the webhook is used for.
     * @type {string}
     * @memberof Webhook
     */
    description?: string | null;
    /**
     * The list of events to enable for this endpoint.
     * @type {Array<string>}
     * @memberof Webhook
     */
    enabled_events: Array<WebhookEnabledEventsEnum>;
    /**
     * Indicates that the webhook is disabled
     * @type {boolean}
     * @memberof Webhook
     */
    disabled?: boolean | null;
    /**
     * Specifies the object type
     * @type {string}
     * @memberof Webhook
     */
    object_type?: string;
    /**
     * The datetime of the last event sent.
     * @type {Date}
     * @memberof Webhook
     */
    last_event_at?: Date | null;
    /**
     * Header signature secret
     * @type {string}
     * @memberof Webhook
     */
    secret: string;
    /**
     * Specified whether it was created with a carrier in test mode
     * @type {boolean}
     * @memberof Webhook
     */
    test_mode: boolean;
}
/**
 * @export
 */
export declare const WebhookEnabledEventsEnum: {
    readonly All: "all";
    readonly ShipmentPurchased: "shipment_purchased";
    readonly ShipmentCancelled: "shipment_cancelled";
    readonly ShipmentFulfilled: "shipment_fulfilled";
    readonly TrackerCreated: "tracker_created";
    readonly TrackerUpdated: "tracker_updated";
    readonly OrderCreated: "order_created";
    readonly OrderUpdated: "order_updated";
    readonly OrderFulfilled: "order_fulfilled";
    readonly OrderCancelled: "order_cancelled";
    readonly OrderDelivered: "order_delivered";
    readonly BatchQueued: "batch_queued";
    readonly BatchFailed: "batch_failed";
    readonly BatchRunning: "batch_running";
    readonly BatchCompleted: "batch_completed";
};
export type WebhookEnabledEventsEnum = typeof WebhookEnabledEventsEnum[keyof typeof WebhookEnabledEventsEnum];
/**
 * Check if a given object implements the Webhook interface.
 */
export declare function instanceOfWebhook(value: object): boolean;
export declare function WebhookFromJSON(json: any): Webhook;
export declare function WebhookFromJSONTyped(json: any, ignoreDiscriminator: boolean): Webhook;
export declare function WebhookToJSON(value?: Webhook | null): any;