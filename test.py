import rdflib
g = rdflib.Graph()
g.parse(data="""
        <x:> a <c:> .
        <y:> a <c:> .
    """,
    format = "turtle")

knows_query = """
SELECT DISTINCT ?s
WHERE {
    ?s a <c:>
}"""

qres = g.query(knows_query)
for row in qres:
    print(row)
# g.serialize(destination="tbl.ttl")