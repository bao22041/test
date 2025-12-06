
import React from "react";
import { useFormik } from "formik";
import { editScheme } from "./validation"; 

const YourForm = () => {
  const formik = useFormik({
    initialValues: {
      title: "",
      description: "",
      price: "",
    },
    validationSchema: editScheme, 
    onSubmit: (values) => {
      console.log("Form data", values);
    },
  });

  return (
    <form onSubmit={formik.handleSubmit}>
      {/* Trường tiêu đề */}
      <div>
        <label htmlFor="title">Title</label>
        <input
          id="title"
          name="title"
          type="text"
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
          value={formik.values.title}
        />
        {formik.errors.title && formik.touched.title && (
          <div>{formik.errors.title}</div>
        )}
      </div>

      {/* Trường mô tả */}
      <div>
        <label htmlFor="description">Description</label>
        <input
          id="description"
          name="description"
          type="text"
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
          value={formik.values.description}
        />
        {formik.errors.description && formik.touched.description && (
          <div>{formik.errors.description}</div>
        )}
      </div>

      {/* Trường giá */}
      <div>
        <label htmlFor="price">Price</label>
        <input
          id="price"
          name="price"
          type="number"
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
          value={formik.values.price}
        />
        {formik.errors.price && formik.touched.price && (
          <div>{formik.errors.price}</div>
        )}
      </div>

      {/* Nút gửi */}
      <div>
        <button type="submit">Submit</button>
      </div>
    </form>
  );
};

export default YourForm;