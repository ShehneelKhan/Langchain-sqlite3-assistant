from dotenv import load_dotenv
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain

load_dotenv()

dburi = "sqlite:///chinook.db"
db = SQLDatabase.from_uri(dburi)
llm = OpenAI(temperature=0)

db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)


db_chain.run("Describe the responses table")
db_chain.run("How many rows is in the responses table of this db?")

