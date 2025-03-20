import aiohttp
import asyncio

async def test_bmi():
    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:5001/bmi", json={"height": 1.75, "weight": 70}) as response:
            data = await response.json()
            assert response.status == 200
            assert data["bmi"] == 22.86

async def test_bmr():
    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:5001/bmr", json={"height": 175, "weight": 70, "age": 30, "gender": "male"}) as response:
            data = await response.json()
            assert response.status == 200
            assert data["bmr"] > 1_800  # Vérification approximative

async def main():
    await test_bmi()
    await test_bmr()

if __name__ == "__main__":
    asyncio.run(main())