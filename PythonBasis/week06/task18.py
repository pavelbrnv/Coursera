class Party:
    name = ''
    votes_number = 0


def get_parties_and_votes():
    read_parties_sign = 'PARTIES:'
    read_votes_sign = 'VOTES:'

    parties = []
    total_votes_number = 0

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
            total_votes_number += 1
    inFile.close()

    return parties, total_votes_number


def main():
    parties, total_votes_number = get_parties_and_votes()
    for party in parties:
        if 0 < party.votes_number \
                and party.votes_number / total_votes_number >= 0.07:
            print(party.name)


main()
