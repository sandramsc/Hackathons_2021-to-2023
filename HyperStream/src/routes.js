// App Name UI Dashboard React layouts
import Settings from "layouts/settings";
import Calendar from "layouts/calendar";
import Dashboard from "layouts/dashboard";
import SignIn from "layouts/authentication/sign-in";
import SignUp from "layouts/authentication/sign-up";

// App Nmae UI Dashboard React icons
import Shop from "examples/Icons/Shop";
import Office from "examples/Icons/Office";
import SettingsIcon from "examples/Icons/Settings";
import Document from "examples/Icons/Document";
import CreditCard from "examples/Icons/CreditCard";
import Cube from "examples/Icons/Cube";
import Goals from "views/Goals/Goals";
import SingleGoal from "views/Goals/SingleGoal";
import Index from "views/Experiment/Index";
import SettingsPage from "views/Settings";
import Calender from "views/Calender";
import SingleGoalGraph from "views/Goals/SingleGoalGraph";

const routes = [
  {
    type: "collapse",
    name: "Dashboard",
    key: "dashboard",
    route: "/dashboard",
    icon: <CreditCard size="12px" />,
    component: <Dashboard />,
    noCollapse: true,
  },
  {
    type: "collapse",
    name: "Goals",
    key: "goals",
    route: "/goals",
    icon: <Office size="12px" />,
    component: <Goals />,
    noCollapse: true,
  },
  {
    type: "collapse",
    name: "Calender",
    key: "calander",
    route: "/calander",
    icon: <CreditCard size="12px" />,
    component: <Calender />,
    noCollapse: true,
  },
  {
    type: "collapse",
    name: "Setting",
    key: "setting",
    route: "/setting",
    icon: <SettingsIcon size="12px" />,
    component: <SettingsPage />,
    noCollapse: true,
  },
];

export default routes;
