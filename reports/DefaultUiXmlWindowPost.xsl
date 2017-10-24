<?xml version="1.0" encoding="iso-8859-1"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output encoding="iso-8859-1" method="xml" indent="yes" />

<xsl:template name="labeldef">
  <xsl:param name="uiwidth"/>
  <xsl:param name="uiposx"/>
  <xsl:param name="uiposy"/>
  <xsl:param name="uidata"/>
  <LabelDef>
    <Color>
      <R>255</R>
      <G>255</G>
      <B>255</B>
      <A>255</A>
    </Color>
    <FontName>arial9</FontName>
    <xsl:choose>
    <xsl:when test="number($uiwidth) = -1">
    <Width><xsl:value-of select="string-length($uidata) * 15"/></Width>
    </xsl:when>
    <xsl:otherwise>
    <Width><xsl:copy-of select="$uiwidth"/></Width>
    </xsl:otherwise>
    </xsl:choose>
    <Height>11</Height>
    <MaxCharacters><xsl:value-of select="string-length($uidata) + 1"/></MaxCharacters>
    <Position>
      <X><xsl:copy-of select="$uiposx"/></X>
      <Y><xsl:copy-of select="$uiposy"/></Y>
    </Position>
    <Data><xsl:copy-of select="$uidata"/></Data>
  </LabelDef>
</xsl:template>

<xsl:template match="label">
  <xsl:call-template name="labeldef">
    <xsl:with-param name="uiwidth"><xsl:value-of select="@width"/></xsl:with-param>
    <xsl:with-param name="uiposx"><xsl:value-of select="@x"/></xsl:with-param>
    <xsl:with-param name="uiposy" select="position() * 12 + 8"/>
    <xsl:with-param name="uidata"><xsl:value-of select="data"/></xsl:with-param>
  </xsl:call-template>
</xsl:template>

<xsl:template match="/Root_Element/WindowTemplate">
  <Root_Element ID="DAOCUi">
    <WindowTemplate>
      <Name>custom1_window</Name>
      <WindowId>custom1_window</WindowId>
      <CloseButton>true</CloseButton>
      <MoveButton>true</MoveButton>
      <Height><xsl:value-of select="count(label) * 12 + 22 "/></Height>
      <Width>384</Width>
      <TitleHeight>18</TitleHeight>
      <TitleWidth>384</TitleWidth>
      <ResizeableWidth>5</ResizeableWidth>
      <ResizeableHeight>5</ResizeableHeight>
      <MinHeight>120</MinHeight>
      <MinWidth>120</MinWidth>
      <BottomRightResizeButton>false</BottomRightResizeButton>
      <BottomLeftResizeButton>false</BottomLeftResizeButton>
      <ResizeButtonOffsetX>9</ResizeButtonOffsetX>

      <FullResizeImageDef>
	<ControlId>Background</ControlId>
	<Height><xsl:value-of select="count(label) * 12 + 22 "/></Height>
	<Width>384</Width>
	<Position>
	  <X>0</X>
	  <Y>0</Y>
	</Position>
	<TemplateName>dlg_background_noresize</TemplateName>
	<Alignment>
	  <GrowWidth>true</GrowWidth>
	  <GrowHeight>true</GrowHeight>
	</Alignment>
      </FullResizeImageDef>

      <LabelDef>
	<Color>
	  <R>255</R>
	  <G>255</G>
	  <B>255</B>
	  <A>255</A>
	</Color>
	<FontName>arial11</FontName>
	<Width>384</Width>
	<Height>16</Height>
	<Position>
	  <X>0</X>
	  <Y>5</Y>
	</Position>
	<MaxCharacters>21</MaxCharacters>
	<Data>Configuration Report</Data>
	<Alignment>
	  <CenterHorizontally>true</CenterHorizontally>
	</Alignment>
      </LabelDef>

      <xsl:apply-templates select="label"/>

    </WindowTemplate>
  </Root_Element>
</xsl:template>

</xsl:stylesheet>


