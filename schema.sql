CREATE TABLE "users" (
    "id" INTEGER,
    "first_name" TEXT,
    "last_name" TEXT,
    "username" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    PRIMARY KEY("id")
);


CREATE TABLE "schools" (
    "school_id" INTEGER,
    "school_name" TEXT NOT NULL,
    "school_location" TEXT,
    "founded" NUMERIC,
    "type" TEXT NOT NULL CHECK("type" IN ('Elementary School','Middle School','High School','College','University','Community College','Other')),
    PRIMARY KEY("school_id")
);

CREATE TABLE "companies" (
    "company_id" INTEGER,
    "company_name" TEXT NOT NULL,
    "company_location" TEXT,
    "industry" TEXT NOT NULL,
    PRIMARY KEY("company_id")
);

CREATE TABLE "user_connections" (
    "person1_id" INTEGER NOT NULL,
    "person2_id" INTEGER NOT NULL,
    PRIMARY KEY("person1_id", person2_id)
    FOREIGN KEY("person1_id") REFERENCES "users"("id"),
    FOREIGN KEY("person2_id") REFERENCES "users"("id"),
);

CREATE TABLE "school_connections" (
    "person_id" INTEGER NOT NULL,
    "school_id" INTEGER NOT NULL,
    "start_date" TEXT,
    "end_date" TEXT,
    "degree" TEXT,
    PRIMARY KEY("person_id", "school_id")
    FOREIGN KEY("person_id") REFERENCES "users"("id"),
    FOREIGN KEY("school_id") REFERENCES "users"("id")
);

CREATE TABLE "company_connections" (
    "person_id" INTEGER NOT NULL,
    "company_id" INTEGER NOT NULL,
    "start_date" TEXT,
    "end_date" TEXT,
    "title" TEXT,
    PRIMARY KEY("person_id", "company_id")
    FOREIGN KEY("person_id") REFERENCES "users"("id"),
    FOREIGN KEY("company_id") REFERENCES "companies"("company_id")
);







