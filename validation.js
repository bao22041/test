import * as yup from "yup";


export const editScheme = yup.object().shape({
  title: yup.string().required("Title is required"), 
  description: yup.string().min(1, "Description is required").required(),
  price: yup
    .number()
    .typeError("Price must be a number")
    .min(1, "Price must be greater than or equal to 1")
    .required("Price is required"),
});