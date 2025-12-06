# E-commerce for Testing

## Backend

1. cd backend
2. Install the project dependencies using `npm install`.
3. Run the web application using `npm dev`.

npm uninstall bcrypt
npm install bcryptjs


## Docker
# Lenh 1: Build Docker Image
cd backend
1. docker build -t ecommerce-be-node .
# Lenh 2: Build Docker Container
2. docker run -p 4000:4000 ecommerce-be-node


## GitHub Actions

This project uses GitHub Actions for continuous integration and deployment. The workflows are defined in the `.github/workflows` directory for both the backend and frontend.

### Backend Workflow

The backend workflow is defined in `backend/.github/workflows/backend.yml`. It includes the following steps:
- Checkout code
- Set up Node.js
- Install dependencies
- Build backend
- Run tests
- Build Docker image
- Deploy to environment

### Frontend Workflow

The frontend workflow is defined in `frontend/.github/workflows/frontend.yml`. It includes the following steps:
- Checkout code
- Set up Node.js
- Install dependencies
- Run tests
- Build frontend
- Build Docker image
- Push Docker image
- Deploy to environment
