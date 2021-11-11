import csv
import os

from sqlalchemy.orm import sessionmaker

from icon_metrics.log import logger
from icon_metrics.models.addresses import Address
from icon_metrics.workers.db import engine


def init_db():
    logger.info(f"Initializing database...")
    SessionMade = sessionmaker(bind=engine)
    session = SessionMade()

    # Import the organization-addresses.csv
    with open(os.path.join(os.path.dirname(__file__), "organization-addresses.csv")) as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            address = session.get(Address, row[0])
            if address is None:
                address = Address()

            address.address = row[0]
            address.organization_wallet = True

            session.add(address)
            session.commit()


if __name__ == "__main__":
    init_db()
