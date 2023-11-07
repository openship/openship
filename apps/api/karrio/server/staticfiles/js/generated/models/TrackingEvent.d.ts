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
 * @interface TrackingEvent
 */
export interface TrackingEvent {
    /**
     * The tracking event's date
     * @type {string}
     * @memberof TrackingEvent
     */
    date?: string;
    /**
     * The tracking event's description
     * @type {string}
     * @memberof TrackingEvent
     */
    description?: string;
    /**
     * The tracking event's location
     * @type {string}
     * @memberof TrackingEvent
     */
    location?: string;
    /**
     * The tracking event's code
     * @type {string}
     * @memberof TrackingEvent
     */
    code?: string | null;
    /**
     * The tracking event's time
     * @type {string}
     * @memberof TrackingEvent
     */
    time?: string | null;
}
/**
 * Check if a given object implements the TrackingEvent interface.
 */
export declare function instanceOfTrackingEvent(value: object): boolean;
export declare function TrackingEventFromJSON(json: any): TrackingEvent;
export declare function TrackingEventFromJSONTyped(json: any, ignoreDiscriminator: boolean): TrackingEvent;
export declare function TrackingEventToJSON(value?: TrackingEvent | null): any;