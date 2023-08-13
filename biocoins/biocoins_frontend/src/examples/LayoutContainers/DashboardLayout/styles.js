// @mui material components
import { makeStyles } from "@mui/styles";

export default makeStyles(({ functions, breakpoints, transitions }) => {
  const { pxToRem } = functions;

  return {
    layoutContainer: {
      position: "relative",
      padding: pxToRem(24),

      [breakpoints.up("xl")]: {
        marginLeft: ({ direction, miniSidenav }) => {
          if (direction === "ltr") {
            return miniSidenav ? pxToRem(120) : pxToRem(274);
          }

          return false;
        },
        marginRight: ({ direction, miniSidenav }) => {
          if (direction === "rtl") {
            return miniSidenav ? pxToRem(120) : pxToRem(274);
          }

          return false;
        },
        transition: transitions.create(["margin-left", "margin-right"], {
          easing: transitions.easing.easeInOut,
          duration: transitions.duration.standard,
        }),
      },
    },
  };
});
