import aiohttp
import asyncio

BINANCE_URL = "https://fapi.binance.com/fapi/v1/time"


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(BINANCE_URL) as response:
            data = await response.json()

            print("Yükseliş Avcısı PRO")
            print("-------------------")
            print("Binance bağlantısı başarılı!")
            print("Binance server time:", data["serverTime"])


if __name__ == "__main__":
    asyncio.run(main())
