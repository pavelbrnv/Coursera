class Party:
    name = ''
    votes_number = 0


def get_parties_and_votes():
    read_parties_sign = 'PARTIES:'
    read_votes_sign = 'VOTES:'

    parties = []

    read_parties_flag = False
    read_votes_flag = False

    inFile = open('input.txt', 'r', encoding='utf8')
    for line in inFile:
        trimmed_line = line.strip()

        if trimmed_line == read_parties_sign:
            read_parties_flag = True
            read_votes_flag = False
            continue
        elif trimmed_line == read_votes_sign:
            read_parties_flag = False
            read_votes_flag = True
            continue

        if read_parties_flag:
            party = Party()
            party.name = trimmed_line
            parties.append(party)

        if read_votes_flag:
            for party in parties:
                if party.name == trimmed_line:
                    party.votes_number += 1
                    break
    inFile.close()

    return parties


def main():
    parties = get_parties_and_votes()
    parties.sort(key=lambda p: (-p.votes_number, p.name))
    for party in parties:
        print(party.name)


main()
