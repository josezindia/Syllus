from allImports import *
from app.logic.getAuthUser import AuthorizedUser
from app.logic.redirectBack import redirect_url
import datetime


@app.route("/deadline/create", methods=["POST"])
def deadlineCreate():
    # we need the page for loggin purposes 
    page = "/" + request.url.split("/")[-1]
    
    # we need the user to know if they are is admin
    authorizedUser = AuthorizedUser()
    if authorizedUser.isAdmin:
        # data contains 
        # deadlineDescription
        data = request.form
	date = datetime.datetime.strptime(data['deadlineDate'],"%m/%d/%Y").date()
        deadline = Deadline.create(
            description=data['deadlineDescription'],
            date=date)
        deadline.save()
        # log the messages
        message = "Deadline: {0} has been added".format(deadline.description)
        log.writer("INFO", page, message)
        flash("Your Deadline has been created")
        return redirect(redirect_url())
    else:
        abort(403)


@app.route("/deadline/edit", methods=["POST"])
def deadlineEdit():
    # we need the page for logging purpuses
    page = "/" + request.url.split("/")[-1]
    authorizedUser = AuthorizedUser()
    if authorizedUser.isAdmin:
        data = request.form

        deadline = Deadline.get(Deadline.id == data['id'])
        deadline.description = data['deadlineDescription']
        deadline.save()

        message = "Deadline: has been edited to {0}".format(
            deadline.description)
        log.writer("INFO", page, message)
        flash("Your Deadline has been edited")
        return redirect(redirect_url())
    else:
        abort(403)


@app.route("/deleteDeadline", methods=["POST"])
def deleteDeadline():
    page = r"/" + request.url.split("/")[-1]
    authorizedUser = AuthorizedUser()
    if authorizedUser.isAdmin:
        data = request.form
        deadline = Deadline.get(Deadline.id == int(data['id']))
        deadline.delete_instance()

        message = "Deadline: {0} has been deleted".format(deadline.description)
        log.writer("INFO", page, message)
        flash("Your Deadline has been deleted")
        return redirect(redirect_url())
    else:
        abort(403)
