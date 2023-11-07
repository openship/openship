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
import type { BatchObject } from './BatchObject';
/**
 *
 * @export
 * @interface BatchOperation
 */
export interface BatchOperation {
    /**
     * A unique identifier
     * @type {string}
     * @memberof BatchOperation
     */
    id?: string;
    /**
     *
     * @type {string}
     * @memberof BatchOperation
     */
    status: BatchOperationStatusEnum;
    /**
     *
     * @type {string}
     * @memberof BatchOperation
     */
    resource_type: BatchOperationResourceTypeEnum;
    /**
     *
     * @type {Array<BatchObject>}
     * @memberof BatchOperation
     */
    resources: Array<BatchObject>;
    /**
     *
     * @type {Date}
     * @memberof BatchOperation
     */
    created_at: Date;
    /**
     *
     * @type {Date}
     * @memberof BatchOperation
     */
    updated_at: Date;
    /**
     *
     * @type {boolean}
     * @memberof BatchOperation
     */
    test_mode: boolean;
}
/**
 * @export
 */
export declare const BatchOperationStatusEnum: {
    readonly Queued: "queued";
    readonly Running: "running";
    readonly Failed: "failed";
    readonly Completed: "completed";
    readonly CompletedWithErrors: "completed_with_errors";
};
export type BatchOperationStatusEnum = typeof BatchOperationStatusEnum[keyof typeof BatchOperationStatusEnum];
/**
 * @export
 */
export declare const BatchOperationResourceTypeEnum: {
    readonly Orders: "orders";
    readonly Shipments: "shipments";
    readonly Trackers: "trackers";
    readonly Billing: "billing";
};
export type BatchOperationResourceTypeEnum = typeof BatchOperationResourceTypeEnum[keyof typeof BatchOperationResourceTypeEnum];
/**
 * Check if a given object implements the BatchOperation interface.
 */
export declare function instanceOfBatchOperation(value: object): boolean;
export declare function BatchOperationFromJSON(json: any): BatchOperation;
export declare function BatchOperationFromJSONTyped(json: any, ignoreDiscriminator: boolean): BatchOperation;
export declare function BatchOperationToJSON(value?: BatchOperation | null): any;