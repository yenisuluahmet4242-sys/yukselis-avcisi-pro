import aiohttp
import asyncio

BINANCE_URL = "https://fapi.binance.com/fapi/v1/exchangeInfo"


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(BINANCE_URL) as response:
            print("HTTP durum kodu:", response.status)

            data = await response.json()

            symbols = []

            for item in data["symbols"]:
                if (
                    item["status"] == "TRADING"
                    and item["contractType"] == "PERPETUAL"
                    and item["quoteAsset"] == "USDT"
                ):
                    symbols.append(item["symbol"])

            print("Yükseliş Avcısı PRO")
            print("-------------------")
            print("Toplam USDT perpetual:", len(symbols))
            print("İlk 20 coin:")

            for symbol in symbols[:20]:
                print(symbol)


if __name__ == "__main__":
    asyncio.run(main())
