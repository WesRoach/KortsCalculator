<?xml version="1.0" encoding="iso-8859-1"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
 xmlns="http://www.w3.org/1999/xhtml" xmlns:math="http://exslt.org/math" 
 version="1.0">
<xsl:output encoding="iso-8859-1" method="xml" 
 doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" 
 doctype-system="DTD/xhtml1-strict.dtd" indent="yes" 
 omit-xml-declaration="yes"/>
<xsl:template name="formatCost">
  <xsl:param name="cost"/>
  <xsl:variable name="plat" select="floor($cost div 10000000)"/>
  <xsl:variable name="gold" select="floor(($cost - $plat * 10000000) div 10000)"/>
  <xsl:variable name="silver" select="floor(($cost - $plat * 10000000 - $gold * 10000) div 100)"/>
  <xsl:variable name="copper" select="floor(($cost - $plat * 10000000 - $gold * 10000 - $silver * 100))"/>
  <xsl:if test="$plat &gt; 0">
    <xsl:copy-of select="$plat"/><xsl:text>p </xsl:text>
  </xsl:if>
  <xsl:if test="$gold &gt; 0 or $plat &gt; 0">
    <xsl:copy-of select="$gold"/><xsl:text>g </xsl:text>
  </xsl:if>
  <xsl:if test="$silver &gt; 0 or $gold &gt; 0 or $plat &gt; 0">
    <xsl:copy-of select="$silver"/><xsl:text>s </xsl:text>
  </xsl:if>
  <xsl:if test="$copper &gt; 0 or $silver &gt; 0 or $gold &gt; 0 or $plat &gt; 0">
    <xsl:copy-of select="$copper"/><xsl:text>c</xsl:text>
  </xsl:if>
</xsl:template>

<xsl:template name="nl">
<xsl:text>
</xsl:text>
</xsl:template>

<xsl:template name="br">
  <xsl:text disable-output-escaping = "yes">&lt;br /&gt;</xsl:text>
</xsl:template>

<xsl:template name="hr">
  <xsl:text disable-output-escaping = "yes">&lt;hr /&gt;</xsl:text>
</xsl:template>

<xsl:template match="SLOT">
  <xsl:variable name="slotnum">
    <xsl:value-of select="number(@Number) + 1"/>
  </xsl:variable>
  <xsl:if test="Type != 'Unused'">
    <xsl:choose>
      <xsl:when test="@Type = 'player'">
	<tr>
	  <td>
            <xsl:text>Gem&#160;</xsl:text><xsl:copy-of select="$slotnum"/>
            <xsl:text>:&#160;</xsl:text>
          </td>
	  <td align="right"><xsl:value-of select="Amount"/>
            <xsl:text>&#160;</xsl:text>
          </td>
	  <td>
	    <xsl:value-of select="Effect"/><xsl:text>&#160;</xsl:text>
	    <xsl:if test="Type != 'Stat' and substring(Type, 1, 3) != 'All'">
	      <xsl:value-of select="Type"/><xsl:text>&#160;</xsl:text>
	    </xsl:if>
	    <xsl:text>- </xsl:text><xsl:value-of select="Qua"/>
            <xsl:text>&#160;</xsl:text>
	    <xsl:value-of select="Name"/>
	  </td>
	</tr>
      </xsl:when>
      <xsl:otherwise>
	<tr>
	  <td>
            <xsl:text>Slot </xsl:text><xsl:copy-of select="$slotnum"/>
            <xsl:text>:&#160;</xsl:text>
          </td>
	  <td align="right"><xsl:value-of select="Amount"/>
            <xsl:text>&#160;</xsl:text>
          </td>
	  <td>
	    <xsl:value-of select="Effect"/><xsl:text>&#160;</xsl:text>
	    <xsl:if test="Type != 'Stat' and Type != 'Other Bonus' and Type != 'PvE Bonus' and Type != 'Other Effect' and substring(Effect, 1, 4) != 'All '">
	      <xsl:value-of select="Type"/><xsl:text>&#160;</xsl:text>
	    </xsl:if>
	    <xsl:if test="Type = 'PvE Bonus'">
	      <xsl:text>(PvE)&#160;</xsl:text>
	    </xsl:if>
	    <xsl:if test="Type = 'Other Effect'">
	      <xsl:text>Effect&#160;</xsl:text>
	    </xsl:if>
	    <xsl:if test="Name != ''">
	      <xsl:text>- </xsl:text><xsl:value-of select="Name"/>
	    </xsl:if>
	    <xsl:text>&#160;</xsl:text>
	  </td>
	</tr>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:if>
</xsl:template>

<xsl:template match="SCItem">
  <xsl:if test="count(SLOT) &gt; 0 and Equipped = '1'">
    <dl>
      <dt><b><xsl:value-of select="Location" /></b></dt>
      <dt>Name: <xsl:value-of select="ItemName"/></dt>
      <dt>
	<xsl:text>Level: </xsl:text><xsl:value-of select="Level"/>
	<xsl:text> &#160; Quality: </xsl:text><xsl:value-of select="ItemQuality"/>
	<xsl:if test="AFDPS != '' and AFDPS != '0' and AFDPS != '-1'">
	  <xsl:text> &#160; AF/DPS: </xsl:text><xsl:value-of select="AFDPS"/>
	</xsl:if>
	<xsl:if test="Speed != '' and Speed != '0' and Speed != '-1' ">
	  <xsl:text> &#160; Speed: </xsl:text><xsl:value-of select="Speed"/>
	</xsl:if>
	<xsl:if test="Bonus != '' and Bonus != '0' and Bonus != '-1' ">
	  <xsl:text> &#160; Bonus: </xsl:text><xsl:value-of select="Bonus"/>
	</xsl:if>
      </dt>
      <xsl:if test="ActiveState = 'player'">
	<dt>
	  <xsl:text>Imbue Points: </xsl:text><xsl:value-of select="Imbue"/>
	  <xsl:text> of </xsl:text><xsl:value-of select="ItemImbue"/>
	  <!--<xsl:text> &#160; Quality: </xsl:text><xsl:value-of select="ItemQuality"/>-->
	  <xsl:text> &#160; Overcharge: </xsl:text>
      <xsl:choose>
	    <xsl:when test="(Imbue - ItemImbue) &lt; 0">
	      <xsl:text>0</xsl:text>
	    </xsl:when>
	    <xsl:otherwise>
		  <xsl:value-of select="Imbue - ItemImbue"/>
		</xsl:otherwise>
	  </xsl:choose>
	</dt>
      </xsl:if>
      <dt>
	<table cellspacing="0" cellpadding="0">
	  <xsl:apply-templates select="SLOT"/>
	</table>
      </dt>
      <dt>
	<xsl:text>Utility: </xsl:text><xsl:value-of select="Utility"/>
        <xsl:if test="ActiveState = 'player'">
	  <xsl:text> &#160; SC Cost: </xsl:text>
	  <xsl:call-template name="formatCost">
	    <xsl:with-param name="cost" select="Cost"/>
	  </xsl:call-template>
	  <xsl:text> &#160; SC Price: </xsl:text>
	  <xsl:call-template name="formatCost">
	    <xsl:with-param name="cost" select="Price"/>
	  </xsl:call-template>
        </xsl:if>
      </dt>
    </dl>
  </xsl:if>
</xsl:template>

<xsl:template name="statsRow">
  <xsl:param name="nodes"/>
  <xsl:variable name="lowercase" select="'abcdefghijklmnopqrstuvwxyz'" />
  <xsl:variable name="uppercase" select="'ABCDEFGHIJKLMNOPQRSTUVWXYZ'" />
  <tr>
    <xsl:for-each select="$nodes">
      <xsl:choose>
	<xsl:when test="name() = 'Hits'">
	  <td>Hits:&#160;</td>
	</xsl:when>
	<xsl:when test="name() = 'Power'">
	  <td>Pow:&#160;</td>
	</xsl:when>
	<xsl:when test="name() = 'PowerPool'">
	  <td>%PP:&#160;</td>
	</xsl:when>
	<xsl:otherwise>
   	  <td><xsl:value-of select="translate(substring(name(),1,3), $lowercase, $uppercase)"/>:&#160;</td>
	</xsl:otherwise>
      </xsl:choose>
      <td align="right">
	<xsl:value-of select="TotalBonus"/>
	<xsl:if test="name() = 'PowerPool'"><xsl:text>%</xsl:text></xsl:if>
	<xsl:text>&#160;</xsl:text>
      </td>
      <td>
	<xsl:text>/ </xsl:text>
	<xsl:value-of select="BaseCap + CapBonus"/>
	<xsl:if test="name() = 'PowerPool'"><xsl:text>%</xsl:text></xsl:if>
        <xsl:text>&#160;</xsl:text>
      </td>
      <td>
	<xsl:if test="TotalCapBonus &gt; 0">
	  <xsl:text>(+</xsl:text><xsl:value-of select="TotalCapBonus"/><xsl:text>)</xsl:text>
	</xsl:if>
        <xsl:text>&#160;</xsl:text>
      </td>
      <td width="10">&#160;&#160;&#160;</td>
    </xsl:for-each>
  </tr>
</xsl:template>

<xsl:template match="Stats">
  <center><b>Stats</b></center>
  <xsl:call-template name="hr"/>
  <table cellspacing="0" cellpadding="0">
    <xsl:call-template name="statsRow">
      <xsl:with-param name="nodes" select="Strength|Intelligence|Hits"/>
    </xsl:call-template>
    <xsl:call-template name="statsRow">
      <xsl:with-param name="nodes" select="Constitution|Piety|AF"/>
    </xsl:call-template>
    <xsl:call-template name="statsRow">
      <xsl:with-param name="nodes" select="Dexterity|Empathy|Power"/>
    </xsl:call-template>
    <xsl:call-template name="statsRow">
      <xsl:with-param name="nodes" select="Quickness|Charisma|PowerPool"/>
    </xsl:call-template>
  </table>
  <xsl:call-template name="br"/>
</xsl:template>

<xsl:template name="resistsRow">
  <xsl:param name="nodes"/>
  <tr>
    <xsl:for-each select="$nodes">
      <td><xsl:value-of select="name()"/><xsl:text>:&#160;</xsl:text></td>
      <td align="right">
	<xsl:value-of select="TotalBonus"/>
        <xsl:text>&#160;</xsl:text>
      </td>
      <td>
	<xsl:text>/ </xsl:text>
	<xsl:value-of select="BaseCap"/>
        <xsl:text>&#160;</xsl:text>
      </td>
      <td>
	<xsl:for-each select="RacialBonus">
          <xsl:text>(+</xsl:text><xsl:value-of select="."/><xsl:text>)</xsl:text>
	</xsl:for-each>
	<xsl:text>&#160;</xsl:text>
      </td>
      <td width="10"><xsl:text>&#160;&#160;&#160;</xsl:text></td>
    </xsl:for-each>
  </tr>
</xsl:template>

<xsl:template match="Resists">
  <center><b>Resists</b></center>
  <xsl:call-template name="hr"/>
  <table cellspacing="0" cellpadding="0">
    <xsl:call-template name="resistsRow">
      <xsl:with-param name="nodes" select="Crush|Body|Energy"/>
    </xsl:call-template>
    <xsl:call-template name="resistsRow">
      <xsl:with-param name="nodes" select="Slash|Cold|Matter"/>
    </xsl:call-template>
    <xsl:call-template name="resistsRow">
      <xsl:with-param name="nodes" select="Thrust|Heat|Spirit"/>
    </xsl:call-template>
    <xsl:call-template name="resistsRow">
      <xsl:with-param name="nodes" select="Essence"/>
    </xsl:call-template>
  </table>
  <xsl:call-template name="br"/>
</xsl:template>

<xsl:template name="bonuslist">
  <xsl:param name="title"/>
  <xsl:param name="nodes"/>
  <center><b><xsl:value-of select="$title"/></b></center>
  <xsl:call-template name="hr"/>
  <table cellspacing="0" cellpadding="0">
    <xsl:for-each select="$nodes">
      <tr>
	<td align="right"><xsl:value-of select="TotalBonus"/>&#160;</td>
	<td>/ <xsl:value-of select="BaseCap"/>&#160;</td>
	<xsl:choose>
	  <xsl:when test="@text != ''">
	    <td><xsl:value-of select="@text"/></td>
	  </xsl:when>
	  <xsl:otherwise>
	    <td><xsl:value-of select="name()"/></td>
	  </xsl:otherwise>
	</xsl:choose>
      </tr>
    </xsl:for-each>
  </table>
  <xsl:call-template name="br"/>
</xsl:template>

<xsl:key name="gemname" use="Name"
         match="/SCTemplate/SCItem/SLOT"/>

<xsl:template name="gemitem">
  <xsl:param name="nodes"/>
  <tr>
    <td align="right">
      <xsl:value-of select="count($nodes)"/>
      <xsl:text>&#160;</xsl:text>
    </td>
    <td><xsl:value-of select="$nodes/Name"/></td>
  </tr>
</xsl:template>

<xsl:template name="gemlist">
  <xsl:param name="nodes"/>
  <xsl:for-each select="$nodes[generate-id(.)=generate-id(key('gemname',Name)[1])]">
    <xsl:sort select="Level" data-type="number"/>
    <xsl:sort select="Type" order="descending"/>
    <xsl:sort select="Name"/>
    <xsl:variable name="onename">
      <xsl:value-of select="Name"/>
    </xsl:variable>
    <xsl:call-template name="gemitem">
      <xsl:with-param name="nodes" select="$nodes[Name=$onename]"/>
    </xsl:call-template>
  </xsl:for-each>
</xsl:template>

<xsl:template name="gems">
  <xsl:param name="nodes"/>
  <center><b>Gem Listing</b></center>
  <xsl:call-template name="hr"/>
  <table cellspacing="0" cellpadding="0">
    <xsl:call-template name="gemlist">
      <xsl:with-param name="nodes" select="$nodes[Level]"/>
    </xsl:call-template>
  </table>
  <xsl:call-template name="br"/>
</xsl:template>

<xsl:key name="matname" use="@Name"
         match="/SCTemplate/SCItem/SLOT/Material"/>

<xsl:template name="materialitem">
  <xsl:param name="nodes"/>
  <tr>
    <td align="right">
      <xsl:value-of select="sum($nodes/@Amount)"/>
      <xsl:text>&#160;</xsl:text>
    </td>
    <td><xsl:value-of select="$nodes/@Name"/></td>
  </tr>
</xsl:template>

<xsl:template name="materiallist">
  <xsl:param name="nodes"/>
  <xsl:for-each select="$nodes[generate-id(.)=generate-id(key('matname',@Name)[1])]">
    <xsl:sort select="@Order"/>
    <xsl:variable name="onename">
      <xsl:value-of select="@Name"/>
    </xsl:variable>
    <xsl:call-template name="materialitem">
      <xsl:with-param name="nodes" select="$nodes[@Name=$onename]"/>
    </xsl:call-template>
  </xsl:for-each>
</xsl:template>

<xsl:template name="materials">
  <xsl:param name="nodes"/>
  <center><b>Materials</b></center>
  <xsl:call-template name="hr"/>
  <table cellspacing="0" cellpadding="0">
    <tr><td colspan="2"><b>Gems</b></td></tr>
    <xsl:call-template name="materiallist">
      <xsl:with-param name="nodes" select="$nodes[@Type='Gems']"/>
    </xsl:call-template>
    <tr><td colspan="2"><b>Liquids</b></td></tr>
    <xsl:call-template name="materiallist">
      <xsl:with-param name="nodes" select="$nodes[@Type='Liquids']"/>
    </xsl:call-template>
    <tr><td colspan="2"><b>Dusts</b></td></tr>
    <xsl:call-template name="materiallist">
      <xsl:with-param name="nodes" select="$nodes[@Type='Dusts']"/>
    </xsl:call-template>
  </table>
  <xsl:call-template name="br"/>
</xsl:template>

<xsl:template match="/SCTemplate">
<html>
<head>
<title>Config Report</title>
</head>
<body>
  <center><b>Config Report</b></center>
  <xsl:call-template name="br"/>
  <xsl:apply-templates select="Stats"/>
  <xsl:apply-templates select="Resists"/>
  <xsl:for-each select="Skills|Focus|OtherBonuses|PvEBonuses">
    <xsl:if test="count(./*) &gt; 0">
      <xsl:choose>
	<xsl:when test="@text != ''">
	  <xsl:call-template name="bonuslist">
	    <xsl:with-param name="title" select="@text"/>
	    <xsl:with-param name="nodes" select="./*"/>
	  </xsl:call-template>
	</xsl:when>
	<xsl:otherwise>
	  <xsl:call-template name="bonuslist">
	    <xsl:with-param name="title" select="name()"/>
	    <xsl:with-param name="nodes" select="./*"/>
	  </xsl:call-template>
	</xsl:otherwise>
      </xsl:choose>
    </xsl:if>
  </xsl:for-each>
  <center><b>Piece Listing</b></center>
  <xsl:call-template name="hr"/>
  <xsl:apply-templates select="SCItem"/>
  <xsl:call-template name="br"/>
  <xsl:call-template name="gems">
    <xsl:with-param name="nodes" select="SCItem/SLOT"/>
  </xsl:call-template>
  <xsl:call-template name="materials">
    <xsl:with-param name="nodes" select="SCItem/SLOT/Material"/>
  </xsl:call-template>
</body>
</html>
</xsl:template>
</xsl:stylesheet>
