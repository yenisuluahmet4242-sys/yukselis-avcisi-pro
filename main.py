import aiohttp
import asyncio

BINANCE_URL = "https://fapi.binance.com/fapi/v1/time"


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(BINANCE_URL) as response:
            print("HTTP durum kodu:", response.status)

            data = await response.text()

            print("Binance cevabı:")
            print(data)


if __name__ == "__main__":
    asyncio.run(main())
