def http_status(status):
  match status:
    case 200:
      return "ok"
    case 404:
      return "not found"
    case 500:
      return "internal server error"
    case _:
      return "unknoen status"
    

print(http_status(500))    