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
import type { Address } from './Address';
/**
 *
 * @export
 * @interface AddressList
 */
export interface AddressList {
    /**
     *
     * @type {number}
     * @memberof AddressList
     */
    count?: number | null;
    /**
     *
     * @type {string}
     * @memberof AddressList
     */
    next?: string | null;
    /**
     *
     * @type {string}
     * @memberof AddressList
     */
    previous?: string | null;
    /**
     *
     * @type {Array<Address>}
     * @memberof AddressList
     */
    results: Array<Address>;
}
/**
 * Check if a given object implements the AddressList interface.
 */
export declare function instanceOfAddressList(value: object): boolean;
export declare function AddressListFromJSON(json: any): AddressList;
export declare function AddressListFromJSONTyped(json: any, ignoreDiscriminator: boolean): AddressList;
export declare function AddressListToJSON(value?: AddressList | null): any;