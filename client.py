# %%
from typedb.client import *

with TypeDB.core_client("localhost:1729") as client:
    with client.session("somalia", SessionType.DATA) as session:
        with session.transaction(TransactionType.READ) as read_transaction:
            answer_iterator = read_transaction.query().match(
                "match $x isa tree; $x has bn $b; $x has uses $j; $x has region 'Somali'; $x has max_alt > 1800;"
            )

            for person in answer_iterator:
                print(
                    "Tree: ",
                    person.get("b").get_value(),
                    " Use: ",
                    person.get("j").get_value(),
                )
