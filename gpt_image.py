import asyncio
from g4f.client import AsyncClient


async def gen():
    client = AsyncClient()

    response = await client.images.generate(
        prompt="a white mercedes",
        model="flux",
        response_format="url"
        # Add any other necessary parameters
    )

    image_url = response.data[0].url
    print(f"Generated image URL: {image_url}")

async def prompt():
    await asyncio.sleep(1)
    print('a white siamese cat')


async def main():
    await asyncio.gather(gen(), prompt())


asyncio.run(main())