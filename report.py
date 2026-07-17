def print_report(groups):

    print()

    print("Scanning Downloads...")

    print()

    total = 0

    for folder, files in groups.items():

        print(folder)

        for file in files:

            print(

                f"    {file.name}"

            )

            total += 1

        print()

    print(

        f"Processed files : {total}"

    )

    print(

        f"Folders created : {len(groups)}"

    )
