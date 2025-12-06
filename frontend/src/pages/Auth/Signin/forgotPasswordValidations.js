
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
} from "@chakra-ui/react";

function ForgotPassword() {
  const [email, setEmail] = useState("");
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    // Logic xử lý gửi email reset mật khẩu
    setSubmitted(true);
  };

  return (
    <Flex align="center" width="full" justifyContent="center">
      <Box pt={10}>
        <Box textAlign="center">
          <Heading>Forgot Password</Heading>
        </Box>
        {submitted ? (
          <Alert status="success" mt={5}>
            Instructions to reset your password have been sent to {email}.
          </Alert>
        ) : (
          <Box my={5} textAlign="left">
            <form onSubmit={handleSubmit}>
              <FormControl>
                <FormLabel>E-mail</FormLabel>
                <Input
                  name="email"
                  type="email"
                  placeholder="Enter your email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                />
              </FormControl>
              <Button mt="4" width="full" type="submit" colorScheme="teal">
                Send Instructions
              </Button>
            </form>
          </Box>
        )}
      </Box>
    </Flex>
  );
}

export default ForgotPassword;