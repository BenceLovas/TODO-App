DROP TABLE IF EXISTS test;

CREATE TABLE test (
    id_ SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    details VARCHAR(255),
    submission_time TIMESTAMP WITH TIME ZONE,
    type VARCHAR(255)
);

