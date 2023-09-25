from sqlalchemy import Column, Integer, String, Float, DateTime, ARRAY
from core.database import Base


class OrdersDatabase(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, nullable=False, unique=True)

    scooter_id = Column(Integer, nullable=False)
    scooter_name = Column(String, nullable=False)

    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)

    start_address = Column(
        ARRAY(
            item_type=Float(
                precision=12,
                decimal_return_scale=10,
            ),
        ),
        nullable=False,
    )
    end_address = Column(
        ARRAY(
            item_type=Float(
                precision=12,
                decimal_return_scale=10,
            ),
        ),
        nullable=False,
    )

    total_price = Column(
        Float(
            precision=5,
            decimal_return_scale=3,
        ),
        nullable=False,
    ),
