CREATE TABLE "passengers" (
    "id" INTEGER,
    "first_name" TEXT,
    "last_name" TEXT,
    "age" NUMERIC,
    PRIMARY KEY("id")
);
CREATE TABLE "airlines" (
    "airline_id" NUMERIC NOT NULL,
    "airline_name" TEXT NOT NULL,
    "concourses" TEXT NOT NULL CHECK("concourses" IN ('A','B','C','D','E','F','T')),
    PRIMARY KEY("airline_id")
);

CREATE TABLE "flights" (
    "id" TEXT,
    "airline_id" NUMERIC NOT NULL,
    "flight_to" TEXT NOT NULL,
    "flight_from" TEXT NOT NULL,
    "arrival" TEXT,
    "departure" TEXT,
    FOREIGN KEY("airline_id") REFERENCES "airlines"("airline_id"),
    PRIMARY KEY("id")
);

CREATE TABLE "checkins" (
    "checkin_id" INTEGER,
    "passenger_id" INTEGER,
    "checkin_time" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "flight_id" TEXT,
    FOREIGN KEY("passenger_id") REFERENCES "passengers"("id"),
    FOREIGN KEY("flight_id") REFERENCES "flights"("id"),
    PRIMARY KEY("checkin_id")
);








