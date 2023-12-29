from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


class SuvlarAPi(APIView):
    def get(self, request):
        suvlar = Suv.objects.all()
        serializer = SuvSerializer(suvlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        suv = request.data
        serializer = SuvSerializer(data=suv)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class SuvAPi(APIView):
    def get(self, request, pk):
        suv = Suv.objects.get(id=pk)
        serializer = SuvSerializer(suv)
        return Response(serializer.data)

    def put(self, request, pk):
        suv = Suv.objects.get(id=pk)
        serializer = SuvSerializer(suv, data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            Suv.objects.filter(id=pk).update(
                brend=data.get("brend"),
                narx=data.get("narx"),
                litr=data.get("litr"),
                batafsil=data.get("batafsil"),
            )
            return Response(serializer.data)
        return Response(serializer.errors)


class MijozlarAPi(APIView):
    def get(self, request):
        mijozlar = Mijoz.objects.all()
        serializer = MijozSerializer(mijozlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        mijozlar = request.data
        serializer = MijozSerializer(data=mijozlar)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class MijozAPi(APIView):
    def get(self, request, pk):
        mijoz = Mijoz.objects.get(id=pk)
        serializer = MijozSerializer(mijoz)
        return Response(serializer.data)

    def put(self, request, pk):
        mijoz = Mijoz.objects.get(id=pk)
        serializer = MijozSerializer(mijoz, data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            Mijoz.objects.filter(id=pk).update(
                ism=data.get("ism"),
                tel=data.get("tel"),
                manzil=data.get("manzil"),
                qarz=data.get("qarz"),
                user=data.get("user"),
            )
            return Response(serializer.data)
        return Response(serializer.errors)


class BuyurtmalarAPi(APIView):
    def get(self, request):
        buyurtmala = Buyurtma.objects.all()
        serializer = BuyurtmaSerializer(buyurtmala, many=True)
        return Response(serializer.data)

    def post(self, request):
        buyurtma = request.data
        serializer = BuyurtmaSerializer(data=buyurtma)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class AdminlarAPi(APIView):
    def get(self, request):
        adminlar = Admin.objects.all()
        serializer = AdminSerializer(adminlar, many=True)
        return Response(serializer.data)


class AdminAPi(APIView):
    def get(self, request, pk):
        admin = Admin.objects.get(id=pk)
        serializer = AdminSerializer(admin)
        return Response(serializer.data)


class HaydovchilarAPi(APIView):
    def get(self, request):
        haydovchilar = Haydovchi.objects.all()
        serializer = HaydovchiSerializer(haydovchilar, many=True)
        return Response(serializer.data)


class HaydovchiAPi(APIView):
    def get(self, request, pk):
        haydovchi = Haydovchi.objects.get(id=pk)
        serializer = HaydovchiSerializer(haydovchi)
        return Response(serializer.data)
