FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /app

COPY . .

RUN dotnet restore ClothingStore.sln

RUN dotnet publish ClothingStore.API/ClothingStore.API.csproj \
    -c Release \
    -o /app/out


FROM mcr.microsoft.com/dotnet/aspnet:8.0-jammy

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libfontconfig1 \
    libfreetype6 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=build /app/out .

ENV ASPNETCORE_URLS=http://+:8080

ENTRYPOINT ["dotnet", "ClothingStore.API.dll"]