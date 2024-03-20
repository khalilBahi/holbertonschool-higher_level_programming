-- Write a script that lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id , cities.name , states.name
    FROM cities
    JOIN hbtn_0d_usa.states ON cities.state_id = states.id
    ORDER BY cities.id ASC;