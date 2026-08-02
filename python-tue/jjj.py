def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"ascharaporn angthong {key}: {value}")
        display_info(name="ALICE", age=30,city="NEW YORK")