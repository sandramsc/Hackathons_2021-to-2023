// @mui material components
import { makeStyles } from "@mui/styles";

export default makeStyles(({ functions, breakpoints }) => {
  const { pxToRem } = functions;

  return {
    footer_list: {
      display: "flex",
      flexWrap: "wrap",
      alignItems: "center",
      justifyContent: "center",
      listStyle: "none",
      padding: 0,
      marginTop: pxToRem(24),
      marginBottom: 0,

      [breakpoints.up("lg")]: {
        marginTop: 0,
      },
    },
  };
});
