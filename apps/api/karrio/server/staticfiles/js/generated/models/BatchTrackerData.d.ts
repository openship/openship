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
import type { TrackingData } from './TrackingData';
/**
 *
 * @export
 * @interface BatchTrackerData
 */
export interface BatchTrackerData {
    /**
     * The list of tracking info to process.
     * @type {Array<TrackingData>}
     * @memberof BatchTrackerData
     */
    trackers: Array<TrackingData>;
}
/**
 * Check if a given object implements the BatchTrackerData interface.
 */
export declare function instanceOfBatchTrackerData(value: object): boolean;
export declare function BatchTrackerDataFromJSON(json: any): BatchTrackerData;
export declare function BatchTrackerDataFromJSONTyped(json: any, ignoreDiscriminator: boolean): BatchTrackerData;
export declare function BatchTrackerDataToJSON(value?: BatchTrackerData | null): any;