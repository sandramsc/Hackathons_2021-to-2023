import { useEffect } from "react";

// react-router-dom components
import { useLocation } from "react-router-dom";

// prop-types is a library for typechecking of props.
import PropTypes from "prop-types";

// Soft UI Assets React components
import SoftBox from "components/SoftBox";

// Soft UI Assets React context
import { useSoftUIController, setLayout } from "context";

function AssetsLayout({ children }) {
  const [controller, dispatch] = useSoftUIController();
  const { miniSidenav } = controller;
  const { pathname } = useLocation();

  useEffect(() => {
    setLayout(dispatch, "assets");
  }, [pathname]);

  return (
    <SoftBox
      sx={({ breakpoints, transitions, functions: { pxToRem } }) => ({
        p: 3,
        position: "relative",

        [breakpoints.up("xl")]: {
          marginLeft: miniSidenav ? pxToRem(120) : pxToRem(274),
          transition: transitions.create(["margin-left", "margin-right"], {
            easing: transitions.easing.easeInOut,
            duration: transitions.duration.standard,
          }),
        },
      })}
    >
      {children}
    </SoftBox>
  );
}

// Typechecking props for the AssetsLayout
AssetsLayout.propTypes = {
  children: PropTypes.node.isRequired,
};

export default AssetsLayout;
