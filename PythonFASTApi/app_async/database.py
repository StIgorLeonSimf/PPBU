from sqlalchemy.ext.asyncio import (create_async_engine,
                                    async_sessionmaker,
                                    )

DATABASE_URL = "sqlite+aiosqlite:///./database.sqlite"
engine = create_async_engine(DATABASE_URL, future=True, echo=True)