from rest_framework.response import Response
from rest_framework import status


def exception_handler(e):
    if len(e.args) == 2:
        response = {
            "message": e.args[0], "status": 'error'}
        return Response(response, status=e.args[1])
    else:
        response = {
            "message": 'Error something went wrong', "status": 'error'}
        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
