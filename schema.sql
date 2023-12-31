CREATE TABLE "users" (
    "id" INTEGER,
    "first_name" TEXT,
    "last_name" TEXT,
    "username" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "schools" (
    "school_id" INTEGER NOT NULL,
    "school_name" TEXT NOT NULL,
    "school_location" TEXT,
    "founded" NUMERIC,
    "type" TEXT NOT NULL CHECK("type" IN ('Elementary School','Middle School','High School','College','University','Community'College,'Other')),
    "degrees" TEXT,
    PRIMARY KEY("school_id")
);

CREATE TABLE "companies" (
    "company_id" INTEGER NOT NULL,
    "company_name" TEXT NOT NULL,
    "company_location" TEXT,
    "industry" TEXT NOT NULL,
    "titles" TEXT;
    PRIMARY KEY("company_id")
);

CREATE TABLE "connections" (
    "connection_id" NUMERIC NOT NULL,
    "school_id" INTEGER,
    "company_id" INTEGER,
    "person_id" INTEGER;
    "start_date" NUMERIC,
    "end_date" NUMERIC,
    "type" TEXT NOT NULL CHECK("type" IN ('School','Company','Person')),
    FOREIGN KEY("company_id") REFERENCES "companies"("company_id"),
    FOREIGN KEY("school_id") REFERENCES "schools"("schoool_id"),
    FOREIGN KEY("person_id") REFERENCES "users"("id"),
    PRIMARY KEY("connection_id")
);
