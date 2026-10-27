"""Print an offline cue sheet; no model calls, photos or network access."""
import argparse, json
SCENES = {
 "walk": [(0,2.5,"Low view: careful steps into glowing petals"),(2.5,5,"Rise to full body as the adult crouches"),(5,7.5,"Scoop petals with both hands"),(7.5,9.5,"Recognizable face above cupped petals"),(9.5,10,"Brief fade"),(10,12,"Complete original portrait frame, steady ending")],
 "hug": [(0,3,"Exactly two adults approach"),(3,6,"Gentle embrace, distinct faces and correct arms"),(6,10,"Hold embrace with a calm camera arc")]
}
def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument("scene",choices=SCENES)
 p.add_argument("--json",action="store_true")
 a=p.parse_args(); steps=[dict(start=s,end=e,cue=c) for s,e,c in SCENES[a.scene]]
 if a.json: print(json.dumps({"scene":a.scene,"seconds":steps[-1]["end"],"steps":steps},indent=2))
 else:
  for x in steps: print(f"{x['start']:>4}-{x['end']:<4}s  {x['cue']}")
if __name__ == "__main__": main()
