pkts = PcapReader(infile)
for p in pkts:
        F = bin(p['TCP'].flags)
        print F, bin(F), p.summary()
        # manual flags extraction from F
