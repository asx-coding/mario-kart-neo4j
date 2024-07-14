MATCH (gp:GrandPrix)-[:HAS_RACE]->(r:Race)
WHERE NOT gp.id IN ["0", "1"]
WITH gp, COUNT(r) as numRaces
SET gp.raceCount = numRaces
;
MATCH (rp:RacePlayer)-[:RACED_IN]->(r:Race)
WITH r, COUNT(rp) as participants
SET r.participants = participants
;