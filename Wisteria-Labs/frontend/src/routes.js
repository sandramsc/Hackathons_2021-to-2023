// Soft UI Dashboard React layouts
import Assets from "layouts/assets";
import Accounts from "layouts/accounts";
import BuySell from "layouts/buy-sell";
import SendReceive from "layouts/send-receive";
// Soft UI Dashboard React icons
import Shop from "examples/Icons/Shop";
import Basket from "examples/Icons/Basket";
import CustomerSupport from "examples/Icons/CustomerSupport";

const routes = [
  {
    type: "collapse",
    name: "Assets",
    key: "assets",
    route: "/assets",
    icon: <Shop size="12px" />,
    component: <Assets />,
    noCollapse: true,
  },
  {
    type: "collapse",
    name: "Buy/Sell",
    key: "buy-sell",
    route: "/buy-sell",
    icon: <Basket size="12px" />,
    component: <BuySell />,
    noCollapse: true,
  },
  {
    type: "collapse",
    name: "Send/Receive",
    key: "send-receive",
    route: "/send-receive",
    icon: <Basket size="12px" />,
    component: <SendReceive />,
    noCollapse: true,
  },
  {
    type: "collapse",
    name: "Accounts",
    key: "accounts",
    route: "/accounts",
    icon: <CustomerSupport size="12px" />,
    component: <Accounts />,
    noCollapse: true,
  },
];

export default routes;
