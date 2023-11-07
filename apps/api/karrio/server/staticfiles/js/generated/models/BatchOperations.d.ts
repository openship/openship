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
import type { BatchOperation } from './BatchOperation';
/**
 *
 * @export
 * @interface BatchOperations
 */
export interface BatchOperations {
    /**
     *
     * @type {number}
     * @memberof BatchOperations
     */
    count?: number | null;
    /**
     *
     * @type {string}
     * @memberof BatchOperations
     */
    next?: string | null;
    /**
     *
     * @type {string}
     * @memberof BatchOperations
     */
    previous?: string | null;
    /**
     *
     * @type {Array<BatchOperation>}
     * @memberof BatchOperations
     */
    results: Array<BatchOperation>;
}
/**
 * Check if a given object implements the BatchOperations interface.
 */
export declare function instanceOfBatchOperations(value: object): boolean;
export declare function BatchOperationsFromJSON(json: any): BatchOperations;
export declare function BatchOperationsFromJSONTyped(json: any, ignoreDiscriminator: boolean): BatchOperations;
export declare function BatchOperationsToJSON(value?: BatchOperations | null): any;