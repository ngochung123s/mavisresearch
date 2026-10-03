"""Robust Europe PMC fetch with retry/backoff (research phase only)."""
import json
import sys
import time
import urllib.parse
import urllib.request


def fetch(query, out, page_size=5, result_type="lite", tries=5):
    params = urllib.parse.urlencode({
        "query": query, "format": "json",
        "resultType": result_type, "pageSize": page_size,
    })
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + params
    last = None
    for a in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "MavisResearch/1.0"})
            with urllib.request.urlopen(req, timeout=30) as r:
                raw = r.read()
            d = json.loads(raw)
            open(out, "w", encoding="utf-8").write(json.dumps(d))
            res = ((d.get("resultList") or {}).get("result")) or []
            print("==", out, "hits:", d.get("hitCount"))
            for x in res[:page_size]:
                print("  ", x.get("pmid"), "|", x.get("pubYear"), "|", (x.get("title") or "")[:95])
            return True
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(3 * (a + 1))
    print("FAILED", out, last)
    return False


if __name__ == "__main__":
    # args: out|query pairs
    ok = True
    i = 1
    while i < len(sys.argv):
        out = sys.argv[i]
        q = sys.argv[i + 1]
        ok = fetch(q, out) and ok
        i += 2
        time.sleep(2)
