import * as yup from "yup";

// Bug - Test Case 2: Check Title Input Field

// const editScheme = yup.object().shape({
//   title: yup.string().required(),
//   description: yup.string().min(5).required(),
//   price: yup.string().required(),
// });

// export default editScheme;

// 
// update validation 1
// import * as yup from "yup";

// fix-bug test case 2

// const editScheme = yup.object().shape({
//   title: yup.string().min(3, "Title must be at least 3 characters").required("Title is required"),
//   description: yup.string().min(5, "Description must be at least 5 characters").required("Description is required"),
//   price: yup.number().required("Price is required").positive("Price must be a positive number").typeError("Price must be a valid number"),
// });

// export default editScheme;

// update validation photo
// fix bug test case 4 




const editScheme = yup.object().shape({
  title: yup.string().required(),
  description: yup.string().min(5).required(),
  price: yup.string().required(),
  title: yup.string().min(3, "Title must be at least 3 characters").required("Title is required"),
  description: yup.string().min(5, "Description must be at least 5 characters").required("Description is required"),
  price: yup.number().required("Price is required").positive("Price must be a positive number").typeError("Price must be a valid number"),
  photos: yup.array()
    .min(1, "At least one photo is required") // Kiểm tra nếu mảng photos có ít nhất một phần tử
    .of(yup.string().url("Each photo URL must be valid")) // Kiểm tra từng phần tử trong mảng là một URL hợp lệ
    .required("Photos are required"), // Mảng photos là bắt buộc
});

export default editScheme;