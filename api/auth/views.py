from django.shortcuts import render

# Create your views here.
# api/user/views.py
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from utils.services.responses import error_response, success_response


class JWTLoginView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="User Login",
        operation_description="Login using txt_login_id and password to get JWT tokens",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["txt_login_id", "password"],
            properties={
                "txt_login_id": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="User Login ID"
                ),
                "password": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format="password",
                    description="User Password"
                ),
            },
        ),
        responses={
            200: openapi.Response(
                description="Login successful",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "message": openapi.Schema(type=openapi.TYPE_STRING),
                        "data": openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                "login_details": openapi.Schema(
                                    type=openapi.TYPE_OBJECT,
                                    properties={
                                        "is_pass_changed": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                                        "is_2fa": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                                    },
                                ),
                                "tokens": openapi.Schema(
                                    type=openapi.TYPE_OBJECT,
                                    properties={
                                        "refresh_token": openapi.Schema(type=openapi.TYPE_STRING),
                                        "access_token": openapi.Schema(type=openapi.TYPE_STRING),
                                    },
                                ),
                            },
                        ),
                    },
                ),
            ),
            400: openapi.Response(
                description="Invalid login ID or password"
            ),
        },
        tags=["Authentication"],
        security=[],  # 🔴 VERY IMPORTANT: disables Bearer token for login
    )
    def post(self, request):
        login_id = request.data.get("txt_login_id")
        password = request.data.get("password")

        user = authenticate(txt_login_id=login_id, password=password)

        if user is None:
            return error_response(
                message="Invalid login ID or password",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        refresh = RefreshToken.for_user(user)

        data = {
            "login_details": {
                "is_pass_changed": user.is_pass_changed,
                "is_2fa": user.is_2fa
            },
            "tokens": {
                "refresh_token": str(refresh),
                "access_token": str(refresh.access_token)
            }
        }

        return success_response(
            message="Login Successful",
            data=data,
            status_code=status.HTTP_200_OK
        )


        
# api/user/views.py
from rest_framework.permissions import IsAuthenticated

class JWTLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
    operation_summary="User Logout",
    operation_description="Logout user by blacklisting refresh token",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["refresh"],
        properties={
            "refresh": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Refresh token to blacklist"
            ),
        },
    ),
    responses={
        200: openapi.Response(
            description="Logout successful",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "status": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                    "message": openapi.Schema(type=openapi.TYPE_STRING),
                }
            ),
        ),
        400: openapi.Response(
            description="Logout failed",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "status": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                    "message": openapi.Schema(type=openapi.TYPE_STRING),
                    "errors": openapi.Schema(type=openapi.TYPE_STRING),
                }
            ),
        ),
    },
    tags=["Authentication"],
    security=[{"Bearer": []}],
)

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")

            if not refresh_token:
                return error_response(
                    message="Refresh token is required",
                    status_code=status.HTTP_400_BAD_REQUEST
                )

            token = RefreshToken(refresh_token)
            token.blacklist()

            return success_response(
                message="Logout successful",
                status_code=status.HTTP_200_OK
            )

        except Exception as e:
            return error_response(
                message="Logout failed",
                errors=str(e),
                status_code=status.HTTP_400_BAD_REQUEST
            )
