import React, { useState } from "react";
import {
  Flex,
  Box,
  Heading,
  FormControl,
  FormLabel,
  Input,
  Button,
  Alert,
  FormErrorMessage,
  Text,
  InputGroup,
  InputRightElement,
  Link,
} from "@chakra-ui/react";
import { FaEye, FaEyeSlash } from "react-icons/fa"; // Import biểu tượng từ react-icons
import { useFormik } from "formik";
import validationSchema from "./validations";
import { fetchLogin } from "../../../api";
import { useAuth } from "../../../contexts/AuthContext";
import { Link as RouterLink } from "react-router-dom"; // Import RouterLink từ react-router-dom : npm install react-router-dom

function Signin({ history }) {
  const { login } = useAuth();
  const [showErrorIndicator, setShowErrorIndicator] = useState(false);
  const [showPassword, setShowPassword] = useState(false);

  const formik = useFormik({
    initialValues: {
      email: "",
      password: "",
    },
    validationSchema,
    onSubmit: async (values, bag) => {
      if (!values.email || !values.password) {
        setShowErrorIndicator(true);
      } else {
        setShowErrorIndicator(false);
      }

      try {
        const loginResponse = await fetchLogin({
          email: values.email,
          password: values.password,
        });
        login(loginResponse);
        history.push("/profile");
      } catch (e) {
        bag.setErrors({ general: e.response.data.message });
      }
    },
  });

  return (
    <div>
      <Flex align="center" width="full" justifyContent="center">
        <Box pt={10}>
          <Box textAlign="center">
            <Heading>Sign In</Heading>
          </Box>
          <Box my={5}>
            {formik.errors.general && (
              <Alert status="error">{formik.errors.general}</Alert>
            )}
          </Box>
          <Box my={5} textAlign="left">
            <form onSubmit={formik.handleSubmit}>
              <FormControl isInvalid={formik.touched.email && formik.errors.email}>
                <FormLabel>
                  E-mail
                  {showErrorIndicator && !formik.values.email && (
                    <Text as="span" color="red.500">
                      *
                    </Text>
                  )}
                </FormLabel>
                <Input
                  name="email"
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  value={formik.values.email}
                />
                <FormErrorMessage>{formik.errors.email}</FormErrorMessage>
              </FormControl>

              <FormControl mt="4" isInvalid={formik.touched.password && formik.errors.password}>
                <FormLabel>
                  Password
                  {showErrorIndicator && !formik.values.password && (
                    <Text as="span" color="red.500">
                      *
                    </Text>
                  )}
                </FormLabel>
                <InputGroup>
                  <Input
                    name="password"
                    type={showPassword ? "text" : "password"}
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                    value={formik.values.password}
                  />
                  <InputRightElement width="4.5rem">
                    <Button
                      h="2rem"
                      w="2rem"
                      p={0}
                      borderRadius="full"
                      bg="gray.200"
                      _hover={{ bg: "gray.300" }}
                      _active={{ bg: "gray.400" }}
                      onClick={() => setShowPassword(!showPassword)}
                    >
                      {showPassword ? <FaEyeSlash /> : <FaEye />}
                    </Button>
                  </InputRightElement>
                </InputGroup>
                <FormErrorMessage>{formik.errors.password}</FormErrorMessage>
              </FormControl>

              <Box mt={2} textAlign="right">
                <Link as={RouterLink} to="/forgot-password" color="teal.500">
                  Quên mật khẩu?
                </Link>
              </Box>

              <Button mt="4" width="full" type="submit">
                Sign In
              </Button>
            </form>
          </Box>
        </Box>
      </Flex>
    </div>
  );
}

export default Signin;