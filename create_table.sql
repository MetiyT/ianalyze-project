
CREATE TABLE JobMarketData (
    ID INT PRIMARY KEY,
    JobTitle NVARCHAR(100),
    Skills NVARCHAR(255),
    Company NVARCHAR(100),
    Location NVARCHAR(100),
    DatePosted DATE
);
