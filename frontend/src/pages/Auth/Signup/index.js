import React, { useState } from "react";
import {
  Flex,
  Box,
  Heading,
  FormControl,
  FormLabel,
  Input,
  InputGroup,
  InputRightElement,
  Button,
  Alert,
  Text,
} from "@chakra-ui/react";
import { useFormik } from "formik";
import validationSchema from "./validations";
import { fetcRegister } from "../../../api";
import { useAuth } from "../../../contexts/AuthContext";

function Signup({ history }) {
  const { login } = useAuth();
  const [showPassword, setShowPassword] = useState(false);
  const [showPasswordConfirm, setShowPasswordConfirm] = useState(false);
  const [successMessage, setSuccessMessage] = useState("");

  const handlePasswordVisibility = () => setShowPassword(!showPassword);
  const handlePasswordConfirmVisibility = () =>
    setShowPasswordConfirm(!showPasswordConfirm);

  const formik = useFormik({
    initialValues: {
      email: "",
      password: "",
      passwordConfirm: "",
    },
    validationSchema,
    onSubmit: async (values, bag) => {
      try {
        const registerResponse = await fetcRegister({
          email: values.email,
          password: values.password,
        });
        if (registerResponse.success) {
          setSuccessMessage("Registration success");
          login(registerResponse.data);
          setTimeout(() => {
            history.push("/profile");
          }, 1500);
        } else {
          bag.setErrors({ general: "Registration failed" });
        }
      } catch (e) {
        bag.setErrors({ general: "Registration failed" });
      }
    },
  });

  return (
    <div>
      <Flex align="center" width="full" justifyContent="center">
        <Box pt={10}>
          <Box textAlign="center">
            <Heading>Sign Up</Heading>
          </Box>
          <Box my={5}>
            {successMessage && (
              <Alert status="success">{successMessage}</Alert>
            )}
            {formik.errors.general && (
              <Alert status="error">{formik.errors.general}</Alert>
            )}
          </Box>
          <Box my={5} textAlign="left">
            <form onSubmit={formik.handleSubmit}>
              <FormControl isInvalid={formik.touched.email && formik.errors.email}>
                <FormLabel>E-mail</FormLabel>
                <Input
                  name="email"
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  value={formik.values.email}
                />
                {formik.touched.email && formik.errors.email && (
                  <Text color="red.500" mt={1}>
                    {formik.errors.email}
                  </Text>
                )}
              </FormControl>

              <FormControl
                mt="4"
                isInvalid={formik.touched.password && formik.errors.password}
              >
                <FormLabel>Password</FormLabel>
                <InputGroup>
                  <Input
                    name="password"
                    type={showPassword ? "text" : "password"}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                    value={formik.values.password}
                  />
                  <InputRightElement width="4.5rem">
                    <Button h="1.75rem" size="sm" onClick={handlePasswordVisibility}>
                      {showPassword ? "😑" : "👁"}
                    </Button>
                  </InputRightElement>
                </InputGroup>
                {formik.touched.password && formik.errors.password && (
                  <Text color="red.500" mt={1}>
                    {formik.errors.password}
                  </Text>
                )}
              </FormControl>

              <FormControl
                mt="4"
                isInvalid={
                  formik.touched.passwordConfirm && formik.errors.passwordConfirm
                }
              >
                <FormLabel>Password Confirm</FormLabel>
                <InputGroup>
                  <Input
                    name="passwordConfirm"
                    type={showPasswordConfirm ? "text" : "password"}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                    value={formik.values.passwordConfirm}
                  />
                  <InputRightElement width="4.5rem">
                    <Button
                      h="1.75rem"
                      size="sm"
                      onClick={handlePasswordConfirmVisibility}
                    >
                      {showPasswordConfirm ? "😑" : "👁"}
                    </Button>
                  </InputRightElement>
                </InputGroup>
                {formik.touched.passwordConfirm &&
                  formik.errors.passwordConfirm && (
                    <Text color="red.500" mt={1}>
                      {formik.errors.passwordConfirm}
                    </Text>
                  )}
              </FormControl>

              <Button mt="4" width="full" type="submit">
                Sign Up
              </Button>
            </form>
          </Box>
        </Box>
      </Flex>
    </div>
  );
}

export default Signup;