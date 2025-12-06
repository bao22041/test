import Joi from 'joi';

/**
 * Schema for validating order data.
 * 
 * @typedef {Object} OrderSchema
 * @property {string} address - The address for the order. This field is required.
 * @property {string[]} items - An array of item identifiers. This field is required.
 */
const OrderSchema = Joi.object({
  address: Joi.string().required(),
  items: Joi.array().items(Joi.string()).required(),
});

export default OrderSchema;
